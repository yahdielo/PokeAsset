function getPage() {
    $(document).ready(function() {
        $('.card').click(function() {
          var href = $(this).data('href');
          window.location.href = href;
        });
      });
}

$(document).ready(function() {
    getPage();
  });