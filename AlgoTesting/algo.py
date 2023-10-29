# base testing code courtesy of article - https://towardsdatascience.com/hands-on-content-based-recommender-system-using-python-1d643bf314e4 - changes made to fit our video game reccomendation format
import matplotlib.pyplot as plt
import numpy as np
from sentence_transformers import SentenceTransformer
import pandas as pd
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA

# Graph Styling
plt.style.use('ggplot')
plt.rcParams['font.family'] = 'sans-serif' 
plt.rcParams['font.serif'] = 'Ubuntu' 
plt.rcParams['font.monospace'] = 'Ubuntu Mono' 
plt.rcParams['font.size'] = 14 
plt.rcParams['axes.labelsize'] = 12 
plt.rcParams['axes.labelweight'] = 'bold' 
plt.rcParams['axes.titlesize'] = 12 
plt.rcParams['xtick.labelsize'] = 12 
plt.rcParams['ytick.labelsize'] = 12 
plt.rcParams['legend.fontsize'] = 12 
plt.rcParams['figure.titlesize'] = 12 
plt.rcParams['image.cmap'] = 'jet' 
plt.rcParams['image.interpolation'] = 'none' 
plt.rcParams['figure.figsize'] = (12, 10) 
plt.rcParams['axes.grid']=True
plt.rcParams['lines.linewidth'] = 2 
plt.rcParams['lines.markersize'] = 8
colors = ['xkcd:pale orange', 'xkcd:sea blue', 'xkcd:pale red', 'xkcd:sage green', 'xkcd:terra cotta', 'xkcd:dull purple', 'xkcd:teal', 'xkcd: goldenrod', 'xkcd:cadet blue',
'xkcd:scarlet']

# Check and prep data
data = pd.read_csv('games.csv')
X = np.array(data['About the game'])
data = data[['Name', 'Genres', 'About the game', 'Tags']]
print(data.head())

# Vectorize the game description for comparision with BERT transformer
game_description_text_data = X
model = SentenceTransformer('distilbert-base-nli-mean-tokens')
embeddings = model.encode(game_description_text_data, show_progress_bar=True)

cos_sim_data = pd.DataFrame(cosine_similarity(embeddings))

def main():
   give_recommendations(2)
   give_reccomendations_with_graph(2)

def give_recommendations(index: int) -> dict:
  """Prints data of game with interest and the reccomended games that are selected based off the Steam game description and genres of the game with interest. For now, choose a random index or manually find int index of game to be

  Args:
      index (int): index of the specefic game that a user is interested in

  Returns:
      dict: return the game with interest, reccomended games, and metadata about them
  """

  index_recomm =cos_sim_data.loc[index].sort_values(ascending=False).index.tolist()[1:6]
  game_recs =  data['Name'].loc[index_recomm].values
  result = {'Games':game_recs,'Index':index_recomm}
  
  print('The game the user has expressed interest for is: %s \n'%(data['Name'].loc[index]))
  k=1
  for game in game_recs:
      print('The number %i recommended game is: %s \n'%(k,game))
      k+=1
  
  print('The Steam description of the game with interest is:\n %s \n'%(data['About the game'].loc[index]))
  k=1
  for q in range(len(game_recs)):
    description_q = data['About the game'].loc[index_recomm[q]]
    print('The Steam description of the number %i recommended game is:\n %s \n'%(k,description_q))
    k=k+1

  print('The genres of the game the user has expressed interest for are:\n %s \n'%(data['Genres'].loc[index]))
  k=1
  for q in range(len(game_recs)):
    plot_q = data['Genres'].loc[index_recomm[q]]
    print('The Genres of the number %i recommended game is:\n %s \n'%(k,plot_q))
    k=k+1
  
  return result

# Graphing
def give_reccomendations_with_graph(index: int):
    plt.figure(figsize=(20, 5))  
    plt.plot(cos_sim_data.loc[index], '.', color='firebrick')
    recomm_index = give_recommendations(index)
    x = recomm_index['Index']
    y = cos_sim_data.loc[index][x].tolist()
    m = recomm_index['Games']
    plt.plot(x, y, '.', color='navy', label='Recommended Games')
    plt.title('Game Played: ' + data['Name'].loc[index])
    plt.xlabel('Game Index')
    k = 0
    for x_i in x:
        plt.annotate('%s' % (m[k]), (x_i, y[k]), fontsize=10)
        k += 1

    plt.ylabel('Cosine Similarity')
    plt.ylim(0, 1)
    plt.show()

if __name__ == "__main__":
    main()