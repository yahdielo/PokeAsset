$.getJSON('../json/ch_vmax_alt_art_psa10.json', function(data) {
  var totalPrice = 0;
  var itemCount = 0;

  // Iterate over the JSON data
  $.each(data, function(index, item) {
    if (item.hasOwnProperty('sold_price')) {
      var price = parseFloat(item.sold_price);
      if (!isNaN(price)) {
        totalPrice += price;
        itemCount++;
      }
    }
  });

  // Calculate the average
  var averagePrice = totalPrice / itemCount;

  console.log('Total Price:', totalPrice);
  console.log('Item Count:', itemCount);
  console.log('Average Price:', averagePrice);

  // Display the average in HTML
  $('#average-price').text(averagePrice.toFixed(2)); // Assuming you have an element with the id "average-price"
});