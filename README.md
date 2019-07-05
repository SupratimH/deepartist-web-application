# DeepArtist Web Application
## An AI bot which can identify artist from paintings
Ever came across a piece of art and not able to recollect the legend behind the creation. DeepArtist AI bot is there for your rescue. Access it through one of the following links. 
* https://find-artist.herokuapp.com
* https://supratimh.github.io/find-artist

## Who is DeepArtist AI bot?
DeepArtist is a Deep Learning model, built with a carefully designed Convolution Neural Network. It has been trained to understand the underlying painting styles of the following legends.

* Vincent van Gogh: (1853 - 1890), Dutch, [Post-Impressionism]
* Edgar Degas: (1834 - 1917), French, [Impressionism]
* Pablo Picasso: (1881 - 1973), Spanish, [Cubism]
* Pierre-Auguste Renoir: (1841 - 1919), French, [Impressionism]
* Albrecht Durer: (1471 - 1528), German, [Northern Renaissance]
* Paul Gauguin: (1848 - 1903), French, [Symbolism,Post-Impressionism]
* Francisco Goya: (1746 - 1828), Spanish, [Romanticism]
* Rembrandt: (1606 - 1669), Dutch, [Baroque]
* Alfred Sisley: (1839 - 1899), French,British, [Impressionism]
* Titian: (1488 - 1576), Italian, [High Renaissance,Mannerism]
* Marc Chagall: (1887 - 1985), French,Jewish,Belarusian, [Primitivism]

The code training the model is available here. Accuracy of the current model on unseen paintings of the above artists is approx 87%.
The model is being improved and trained on sample paintings of more artists.

## What does this repo contain?
The code to deploy DeepArtist (or any ML or DL model, for that matter) on cloud, as a web application. At present, it is deployed on Heroku and can be accessed through the links provided above.

## Instructions to use DeepArtist Bot application
1. Open the application through the links provided above.
2. From web, copy the url/location/address of the image jpeg or png file (usually by right click on the image --> copy image address option). The list of artists it can identify are provided above.
3. Paste the url in text box and click "Who's the artist?" button.
4. That's it. DeepArtist Bot will read the image from url, run prediction on it and show the probable artist name and accuracy probability.
