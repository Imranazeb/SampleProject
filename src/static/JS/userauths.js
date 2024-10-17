const csrftoken = getCookie("csrftoken");

$(document).ready(function () {
  console.log("ready");
  console.log(csrftoken);
});

var timer;

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

$("#username").on("keyup", function (e) {
  clearTimeout(timer);

  var textInput = $(e.target);

  timer = setTimeout(function () {
    var value = textInput.val().trim();
    if (value === "") {
      alertBlank();
      return;
    }
    $.ajax({
      url: "/userauths/check",
      headers: { "X-CSRFToken": csrftoken },
      mode: "same-origin",
      method: "GET",
      dataType: "json",
      data: { username: value },
      success: function (res) {
        if (res.success) {
          alertSuccess();
        } else {
          alertWarning();
        }
      },
      error: function (err) {
        console.log(err);
      },
    });
  }, 1000);
});

function alertWarning() {
  $("#alertIcon").addClass("fa-solid fa-triangle-exclamation text-warning ms-2");
  $("alertIcon").removeClass("fa-solid fa-check-circle text-success ms-2");
  document.getElementById("submitButton").disabled = true;
}

function alertSuccess() {
  $("#alertIcon").removeClass("fa-solid fa-triangle-exclamation text-warning ms-2");
  $("#alertIcon").addClass("fa-solid fa-check-circle text-success ms-2");
  document.getElementById("submitButton").disabled = false;
}

function alertBlank() {
  $("#alertIcon").removeClass("fa-solid fa-triangle-exclamation text-warning ms-2");
  $("#alertIcon").removeClass("fa-solid fa-check-circle text-success ms-2");
  document.getElementById("submitButton").disabled = true;
}
