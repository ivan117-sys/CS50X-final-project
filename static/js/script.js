const list = {

    params : {
      
    title: '',
    review: null,

  },



  init() {

    console.log(this.params)

    this.fillStars()

    

  },

  fillStars() {

    $('.card').on('click', (e) => {

      const card = $(e.target).closest('.card')
      const stars = card.find('.la-star')
      const rating = $(e.target).attr('value');
      const title = $(e.target).closest('h3').attr('value');

      this.params.title = title

      console.log(this.title)
    

      stars.each((index, star) => {

        if (rating > index) star.classList.add('fill') 
        if (rating <= index) star.classList.remove('fill')

        this.params.review = rating

        
      })
      console.log(this.title)
      this.sendRating(card)
    
    })
  },

  async sendRating(card) {
    
    console.log(this.params)

    try {

      const response = await fetch('/', {
        method: "POST",
        body: JSON.stringify(this.params),
        headers: {"Content-Type": "application/json"},
        credentials: "same-origin"
      });

      const rating = await response.json();

      const parsedRating = Object.values(rating[0])[0]

      console.log(card.find('.review-grade'))

      card.find('.review-grade').text(parsedRating + ' ' + '/ 5');

      console.log($('.review-grade'))

    } catch (error) {
      console.log(error);
    }
    

  }

}

$(document).ready(list.init());