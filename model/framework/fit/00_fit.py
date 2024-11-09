import csv
import os
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from umap import UMAP
from openTSNE import TSNE
from eosce.models import ErsiliaCompoundEmbeddings
import joblib

print("Done with imports")

ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(ROOT, "data", "drugbank_inchikeys.csv"), "r") as f:
    reader = csv.reader(f)
    next(reader)
    smiles_list = [row[0] for row in reader]

print("Number of SMILES strings:", len(smiles_list))

print("Calculating Ersilia Compound Embeddings...")
embedder = ErsiliaCompoundEmbeddings()
X = embedder.transform(smiles_list)

print("Calculating PCA...")
pca = PCA(n_components=100)
pca.fit(X)
X_pca = pca.transform(X)

print("Calculating UMAP...")
umap = UMAP(n_components=2)
umap.fit(X_pca)
X_umap = umap.transform(X_pca)

print("Calculating tSNE")
tsne = TSNE(n_components=2)
tsne = tsne.fit(X_pca)
X_tsne = tsne.transform(X_pca)

print("Saving reducers")
f = os.path.join(ROOT, "..", "..", "checkpoints", "pca.joblib")
joblib.dump(pca, f)
f = os.path.join(ROOT, "..", "..", "checkpoints", "umap.joblib")
joblib.dump(umap, f)
f = os.path.join(ROOT, "..", "..", "checkpoints", "tsne.joblib")
joblib.dump(tsne, f)

print("Scalers")
pca_scaler = MinMaxScaler(feature_range=(-1, 1))
umap_scaler = MinMaxScaler(feature_range=(-1, 1))
tsne_scaler = MinMaxScaler(feature_range=(-1, 1))
pca_scaler.fit(X_pca[:, :4])
umap_scaler.fit(X_umap)
tsne_scaler.fit(X_tsne)

print("Saving scalers")
f = os.path.join(ROOT, "..", "..", "checkpoints", "pca_scaler.joblib")
joblib.dump(pca_scaler, f)
f = os.path.join(ROOT, "..", "..", "checkpoints", "umap_scaler.joblib")
joblib.dump(umap_scaler, f)
f = os.path.join(ROOT, "..", "..", "checkpoints", "tsne_scaler.joblib")
joblib.dump(tsne_scaler, f)