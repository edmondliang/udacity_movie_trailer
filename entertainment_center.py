#import necessary module
import media
import fresh_tomatoes

#create Movies instance
movies=media.Movies()

#add some movies into movies instance
movies.add("Chappie",
                      "AIn the near future, crime is patrolled by a mechanized police force. When one police droid, Chappie, is stolen and given new programming, he becomes the first robot with the ability to think and feel for himself.",
                      "http://ia.media-imdb.com/images/M/MV5BMTUyNTI4NTIwNl5BMl5BanBnXkFtZTgwMjQ4MTI0NDE@._V1_SX214_AL_.jpg",
                      "https://www.youtube.com/watch?v=m7lBDHaY4M0"
                      )
movies.add("Teddy 2",
                      "Ted must prove his personhood in a court of law so that he and his wife can adopt a baby.",
                      "http://t3.gstatic.com/images?q=tbn:ANd9GcSdyBLpMOpQNRmHVYBa3N1XanSp0K_RRkbJes7fOpQ78coBtYEQ",
                      "https://www.youtube.com/watch?v=eDgUgY8lKlk"
                      )

movies.add("Cinderella",
                      "When her father unexpectedly passes away, young Ella finds herself at the mercy of her cruel stepmother and her daughters. Never one to give up hope, Ella's fortunes begin to change after meeting a dashing stranger.",
                      "http://ia.media-imdb.com/images/M/MV5BMjMxODYyODEzN15BMl5BanBnXkFtZTgwMDk4OTU0MzE@._V1_SX214_AL_.jpg",
                      "https://www.youtube.com/watch?v=cvqgYhCSAN4"
                      )

movies.add("The Imitation Game",
                      "During World War II, mathematician Alan Turing tries to crack the enigma code with help from fellow mathematicians.",
                      "http://ia.media-imdb.com/images/M/MV5BNDkwNTEyMzkzNl5BMl5BanBnXkFtZTgwNTAwNzk3MjE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                      "https://www.youtube.com/watch?v=S5CjKEFb-sM"
                      )

#create static html file and open in browser
fresh_tomatoes.open_movies_page(movies.store)
