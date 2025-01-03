# imports
import os
import sys
import csv
import joblib
from eosce.models import ErsiliaCompoundEmbeddings

ROOT = os.path.abspath(os.path.dirname(__file__))

# loading methods
embedder = ErsiliaCompoundEmbeddings()
f = os.path.join(ROOT, "..", "..", "checkpoints", "pca.joblib")
pca = joblib.load(f)
f = os.path.join(ROOT, "..", "..", "checkpoints", "umap.joblib")
umap = joblib.load(f)
f = os.path.join(ROOT, "..", "..", "checkpoints", "tsne.joblib")
tsne = joblib.load(f)
f = os.path.join(ROOT, "..", "..", "checkpoints", "pca_scaler.joblib")
pca_scaler = joblib.load(f)
f = os.path.join(ROOT, "..", "..", "checkpoints", "umap_scaler.joblib")
umap_scaler = joblib.load(f)
f = os.path.join(ROOT, "..", "..", "checkpoints", "tsne_scaler.joblib")
tsne_scaler = joblib.load(f)

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

print(len(smiles_list))

# calculate embeddings
X = embedder.transform(smiles_list)
print(X.shape)

# make projections
X_pca = pca.transform(X)
X_umap = umap.transform(X_pca)
X_tsne = tsne.transform(X_pca)

# scale projections
X_pca = pca_scaler.transform(X_pca[:, :4])
X_umap = umap_scaler.transform(X_umap)
X_tsne = tsne_scaler.transform(X_tsne)

# assemble dataset
columns = [
    "pca_1",
    "pca_2",
    "pca_3",
    "pca_4",
    "umap_1",
    "umap_2",
    "tsne_1",
    "tsne_2"
]

outputs = []
for i in range(len(smiles_list)):
    outputs += [list(X_pca[i]) + list(X_umap[i]) + list(X_tsne[i])]

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(columns)  # header
    for o in outputs:
        writer.writerow(o)
