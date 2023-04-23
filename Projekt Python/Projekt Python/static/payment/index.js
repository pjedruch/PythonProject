var stripe = Stripe(STRIPE_PUBLISHABLE_KEY);

var elem = document.getElementById('submit');

clientsecret = elem.getAttribute('data-secret');
var elements = stripe.elements();
var style = {
  base: {
    color: "#000",
    lineHeight: '2.4',
    fontSize: '16px'
  }
};

var card = elements.create("card", { style: style });
card.mount("#card-element");

card.on('change', function (event) {
  var displayError = document.getElementById('card-errors')
  if (event.error) {
    displayError.textContent = event.error.message;
    $('#card-errors').addClass('alert alert-info');
  } else {
    displayError.textContent = '';
    $('#card-errors').removeClass('alert alert-info');
  }
});

var payment_type = $('#payment_type')
payment_type.on('change', function (event) {
  var paymentCard = $('#payment_type_card')
  if (payment_type.val() === 'card') {
    paymentCard.show()
  } else {
    paymentCard.hide()
  }
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
  ev.preventDefault();

  var custName = document.getElementById("custName").value;
  var custAdd = document.getElementById("custAdd").value;
  var custAdd2 = document.getElementById("custAdd2").value;
  var postCode = document.getElementById("postCode").value;
  var phone = document.getElementById("phone").value;

  if (!custName || !custAdd || !custAdd2 || !postCode || !phone) {
    return
  }
  var payment_type = $('#payment_type')

  $.ajax({
    type: "POST",
    url: '/orders/add/',
    data: {
      order_key: clientsecret,
      csrfmiddlewaretoken: CSRF_TOKEN,

      full_name: custName,
      address1: custAdd,
      address2: custAdd2,
      post_code: postCode,
      phone: phone,
      payment_type: payment_type.val(),
    },
    success: function (json) {
      console.log(json.success)

      if (payment_type.val() === 'cash') {
        window.location.href = "/users/dashboard/"
        return
      }
      
      stripe.confirmCardPayment(clientsecret, {
        payment_method: {
          card: card,
          billing_details: {
            address: {
              line1: custAdd,
              line2: custAdd2
            },
            name: custName
          },
        }
      }).then(function (result) {
        if (result.error) {
          console.log('payment error')
          console.log(result.error.message);
        } else {
          if (result.paymentIntent.status === 'succeeded') {
            console.log('payment processed')
            window.location.replace("http://127.0.0.1:8000/payment/orderplaced/");
          }
        }
      });

    },
    error: function (xhr, errmsg, err) { },
  })

})