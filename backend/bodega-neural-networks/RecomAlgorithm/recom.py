# %% [code] {"_kg_hide-input":false,"execution":{"iopub.status.busy":"2022-06-27T22:08:15.114831Z","iopub.execute_input":"2022-06-27T22:08:15.115159Z","iopub.status.idle":"2022-06-27T22:08:15.120529Z","shell.execute_reply.started":"2022-06-27T22:08:15.115105Z","shell.execute_reply":"2022-06-27T22:08:15.119624Z"},"jupyter":{"outputs_hidden":false}}
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import matplotlib.image as mpimg
import numpy as np 
import pandas as pd
import os


# %% [code] {"_kg_hide-input":false,"execution":{"iopub.status.busy":"2022-06-27T22:08:15.130674Z","iopub.execute_input":"2022-06-27T22:08:15.130917Z","iopub.status.idle":"2022-06-27T22:08:15.143217Z","shell.execute_reply.started":"2022-06-27T22:08:15.130873Z","shell.execute_reply":"2022-06-27T22:08:15.141992Z"},"jupyter":{"outputs_hidden":false}}
DATASET_PATH = "/Users/rahultiwari/Downloads/fashion-dataset"
print(os.listdir(DATASET_PATH))

# %% [code] {"execution":{"iopub.status.busy":"2022-06-27T22:08:15.210045Z","iopub.execute_input":"2022-06-27T22:08:15.210382Z","iopub.status.idle":"2022-06-27T22:08:15.361231Z","shell.execute_reply.started":"2022-06-27T22:08:15.210329Z","shell.execute_reply":"2022-06-27T22:08:15.360077Z"},"jupyter":{"outputs_hidden":false}}
df = pd.read_csv(DATASET_PATH + "/styles.csv", nrows=5000, error_bad_lines=False)
df['image'] = df.apply(lambda row: str(row['id']) + ".jpg", axis=1)
df = df.reset_index(drop=True)
df.head(10)

# %% [code] {"execution":{"iopub.status.busy":"2022-06-27T22:08:15.363637Z","iopub.execute_input":"2022-06-27T22:08:15.364146Z","iopub.status.idle":"2022-06-27T22:08:15.376677Z","shell.execute_reply.started":"2022-06-27T22:08:15.363939Z","shell.execute_reply":"2022-06-27T22:08:15.375210Z"},"jupyter":{"outputs_hidden":false}}
import cv2
def plot_figures(figures, nrows = 1, ncols=1,figsize=(8, 8)):
    

    fig, axeslist = plt.subplots(ncols=ncols, nrows=nrows,figsize=figsize)
    for ind,title in enumerate(figures):
        axeslist.ravel()[ind].imshow(cv2.cvtColor(figures[title], cv2.COLOR_BGR2RGB))
        axeslist.ravel()[ind].set_title(title)
        axeslist.ravel()[ind].set_axis_off()
    plt.tight_layout() # optional
    
def img_path(img):
    return DATASET_PATH+"/images"+img

def load_image(img, resized_fac = 0.1):
    img     = cv2.imread(img_path(img))
    w, h, _ = img.shape
    resized = cv2.resize(img, (int(h*resized_fac), int(w*resized_fac)), interpolation = cv2.INTER_AREA)
    return resized

# %% [code] {"execution":{"iopub.status.busy":"2022-06-27T22:08:15.378327Z","iopub.execute_input":"2022-06-27T22:08:15.379061Z","iopub.status.idle":"2022-06-27T22:08:16.149096Z","shell.execute_reply.started":"2022-06-27T22:08:15.379007Z","shell.execute_reply":"2022-06-27T22:08:16.148256Z"},"jupyter":{"outputs_hidden":false}}
import matplotlib.pyplot as plt
import numpy as np

figures = {'im'+str(i): load_image(row.image) for i, row in df.sample(6).iterrows()}

plot_figures(figures, 2, 3)

# %% [code] {"execution":{"iopub.status.busy":"2022-06-27T22:08:16.150396Z","iopub.execute_input":"2022-06-27T22:08:16.150799Z","iopub.status.idle":"2022-06-27T22:08:17.986048Z","shell.execute_reply.started":"2022-06-27T22:08:16.150751Z","shell.execute_reply":"2022-06-27T22:08:17.985138Z"},"jupyter":{"outputs_hidden":false}}
plt.figure(figsize=(7,20))
df.articleType.value_counts().sort_values().plot(kind='barh')

# %% [code] {"execution":{"iopub.status.busy":"2022-06-27T22:08:17.990139Z","iopub.execute_input":"2022-06-27T22:08:17.990777Z","iopub.status.idle":"2022-06-27T22:08:18.000919Z","shell.execute_reply.started":"2022-06-27T22:08:17.990718Z","shell.execute_reply":"2022-06-27T22:08:17.999706Z"},"jupyter":{"outputs_hidden":false}}
import tensorflow as tf
import keras
from keras import Model
from tensorflow.keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from tensorflow.keras.layers import GlobalMaxPooling2D
tf.__version__

# %% [code] {"execution":{"iopub.status.busy":"2022-06-27T22:08:18.003414Z","iopub.execute_input":"2022-06-27T22:08:18.004138Z","iopub.status.idle":"2022-06-27T22:08:18.012056Z","shell.execute_reply.started":"2022-06-27T22:08:18.003756Z","shell.execute_reply":"2022-06-27T22:08:18.010661Z"},"jupyter":{"outputs_hidden":false}}
# Input Shape
img_width, img_height, _ = 224, 224, 3

# %% [code] {"execution":{"iopub.status.busy":"2022-06-27T22:08:18.013986Z","iopub.execute_input":"2022-06-27T22:08:18.014336Z","iopub.status.idle":"2022-06-27T22:08:28.025202Z","shell.execute_reply.started":"2022-06-27T22:08:18.014270Z","shell.execute_reply":"2022-06-27T22:08:28.024351Z"},"jupyter":{"outputs_hidden":false}}
base_model = tf.keras.applications.ResNet50( include_top= False, weights ='imagenet',  input_shape = (img_width, img_height, 3))

# %% [code] {"execution":{"iopub.status.busy":"2022-06-27T22:08:28.029027Z","iopub.execute_input":"2022-06-27T22:08:28.029300Z","iopub.status.idle":"2022-06-27T22:08:30.159501Z","shell.execute_reply.started":"2022-06-27T22:08:28.029241Z","shell.execute_reply":"2022-06-27T22:08:30.158685Z"},"jupyter":{"outputs_hidden":false}}
model = tf.keras.Sequential([base_model, GlobalMaxPooling2D()])

model.summary()

# %% [code] {"execution":{"iopub.status.busy":"2022-06-27T22:08:30.161235Z","iopub.execute_input":"2022-06-27T22:08:30.161573Z","iopub.status.idle":"2022-06-27T22:08:30.171025Z","shell.execute_reply.started":"2022-06-27T22:08:30.161496Z","shell.execute_reply":"2022-06-27T22:08:30.170103Z"},"jupyter":{"outputs_hidden":false}}
def get_embedding(model, img_name):
    # Reshape
    img = image.load_img(img_path(img_name), target_size=(img_width, img_height))
    # img to Array
    x   = image.img_to_array(img)
    # Expand Dim (1, w, h)
    x   = np.expand_dims(x, axis=0)
    # Pre process Input
    x   = preprocess_input(x)
    return model.predict(x).reshape(-1)

# %% [code] {"execution":{"iopub.status.busy":"2022-06-27T22:08:30.174030Z","iopub.execute_input":"2022-06-27T22:08:30.174438Z","iopub.status.idle":"2022-06-27T22:08:32.510900Z","shell.execute_reply.started":"2022-06-27T22:08:30.174308Z","shell.execute_reply":"2022-06-27T22:08:32.509882Z"},"jupyter":{"outputs_hidden":false}}
emb = get_embedding(model, df.iloc[0].image)
emb.shape

# %% [code] {"execution":{"iopub.status.busy":"2022-06-27T22:08:32.512146Z","iopub.execute_input":"2022-06-27T22:08:32.512457Z","iopub.status.idle":"2022-06-27T22:08:32.831387Z","shell.execute_reply.started":"2022-06-27T22:08:32.512413Z","shell.execute_reply":"2022-06-27T22:08:32.830534Z"},"jupyter":{"outputs_hidden":false}}
img_array = load_image(df.iloc[0].image)
plt.imshow(cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB))
print(img_array.shape)
print(emb)

# %% [code] {"execution":{"iopub.status.busy":"2022-06-27T22:08:32.832994Z","iopub.execute_input":"2022-06-27T22:08:32.833655Z","iopub.status.idle":"2022-06-27T22:08:32.841488Z","shell.execute_reply.started":"2022-06-27T22:08:32.833573Z","shell.execute_reply":"2022-06-27T22:08:32.840412Z"},"jupyter":{"outputs_hidden":false}}
df.shape

# %% [code] {"execution":{"iopub.status.busy":"2022-06-27T22:08:32.843375Z","iopub.execute_input":"2022-06-27T22:08:32.844156Z"},"jupyter":{"outputs_hidden":false}}
#%%time



df_sample      = df#.sample(10)
map_embeddings = df_sample['image'].apply(lambda img: get_embedding(model, img))
df_embs        = map_embeddings.apply(pd.Series)

print(df_embs.shape)
df_embs.head()

# %% [markdown]
# #### Compute Similarity Between Items

# %% [code] {"jupyter":{"outputs_hidden":false}}

from sklearn.metrics.pairwise import pairwise_distances


cosine_sim = 1-pairwise_distances(df_embs, metric='cosine')
cosine_sim[:4, :4]

# %% [markdown]
# #### Recommender Similar Items

# %% [code] {"jupyter":{"outputs_hidden":false}}
indices = pd.Series(range(len(df)), index=df.index)
indices


def get_recommender(idx, df, top_n = 5):
    sim_idx    = indices[idx]
    sim_scores = list(enumerate(cosine_sim[sim_idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    idx_rec    = [i[0] for i in sim_scores]
    idx_sim    = [i[1] for i in sim_scores]
    
    return indices.iloc[idx_rec].index, idx_sim

get_recommender(2993, df, top_n = 5)

# %% [code] {"jupyter":{"outputs_hidden":false}}
# Idx Item to Recommender
idx_ref = 2993

# Recommendations
idx_rec, idx_sim = get_recommender(idx_ref, df, top_n = 6)

# Plot

plt.imshow(cv2.cvtColor(load_image(df.iloc[idx_ref].image), cv2.COLOR_BGR2RGB))

# generation of a dictionary of (title, images)
figures = {'im'+str(i): load_image(row.image) for i, row in df.loc[idx_rec].iterrows()}
# plot of the images in a figure, with 2 rows and 3 columns
plot_figures(figures, 2, 3)

# %% [code] {"jupyter":{"outputs_hidden":false}}
idx_ref = 878

# Recommendations
idx_rec, idx_sim = get_recommender(idx_ref, df, top_n = 6)


plt.imshow(cv2.cvtColor(load_image(df.iloc[idx_ref].image), cv2.COLOR_BGR2RGB))


figures = {'im'+str(i): load_image(row.image) for i, row in df.loc[idx_rec].iterrows()}
# plot of the images in a figure, with 2 rows and 3 columns
plot_figures(figures, 2, 3)

# %% [code] {"jupyter":{"outputs_hidden":false}}
idx_ref = 987

# Recommendations
idx_rec, idx_sim = get_recommender(idx_ref, df, top_n = 6)

# Plot

plt.imshow(cv2.cvtColor(load_image(df.iloc[idx_ref].image), cv2.COLOR_BGR2RGB))

# generation of a dictionary of (title, images)
figures = {'im'+str(i): load_image(row.image) for i, row in df.loc[idx_rec].iterrows()}
# plot of the images in a figure, with 2 rows and 3 columns
plot_figures(figures, 2, 3)

# %% [code] {"jupyter":{"outputs_hidden":false}}
idx_ref = 3524

# Recommendations
idx_rec, idx_sim = get_recommender(idx_ref, df, top_n = 6)

# Plot

plt.imshow(cv2.cvtColor(load_image(df.iloc[idx_ref].image), cv2.COLOR_BGR2RGB))


figures = {'im'+str(i): load_image(row.image) for i, row in df.loc[idx_rec].iterrows()}

plot_figures(figures, 2, 3)

# %% [markdown]
# ### Bhaiya i am going to sleep. the model is trained well and good. See above for some of the output it spit when input with reference image. 
# **happy anniversary lol**

# %% [code] {"jupyter":{"outputs_hidden":false}}
### i have also downloaded the notebook to your system. if you want python script rather than jupter notebook, you can click on top left "file" change editor type to python script and then download it. If by the time you come and notebook gets reloaded, then click run-all and leave it for 10 mins. it will spit out recommendations

# %% [markdown]
# **if you wanna play with the recommendations, change idx_ref from 0 to 40000 images you have, and see relative recommendations. **

# %% [markdown]
# 