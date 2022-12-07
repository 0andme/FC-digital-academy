let url = "https://jsonplaceholder.typicode.com/posts";

$(document).ready(function () {
  $(".list-group-item").click(function (e) {
    const thisEl = $(this);
    const dataId = $(this).data("id");

    $.get(`${url}/${dataId}`).then((data) => {
      $("#exampleModalLabel").text(data.title);
      $("#modalContent").text(data.body);
      $("#exampleModal").modal("show");
    });
  });
});
