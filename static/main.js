const getotp_btn = document.querySelector("button.get-otp");

function validateEmail(email) {
    return /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(email);
}

getotp_btn.addEventListener("click", (event) => {
    event.preventDefault();

    let token = document.querySelector("input[type=hidden][name=csrfmiddlewaretoken]").value;
    let email = document.getElementById("rg-email").value;

    // check if the email id is null
    if (email.toString().trim() === "") {
        alert("Please, Enter the email");
        return;
    }
    // validate email id
    if(!validateEmail(email)) {
        alert("You have entered an invalid email address!");
        return;
    }

    // send verification email to the user
    $.ajax({
        type: "post",
        url: "http://127.0.0.1:8000/get-otp/",
        data: {
            csrfmiddlewaretoken: token,
            email: email,
        },
        success: function (response) {
            if (response.status) alert("OTP sent successfully.");
            else alert("Something went wrong! please, try again");
        }
    });
});