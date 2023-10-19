const $btnSignIn = document.querySelector('.sign-in-button'),
      $btnSignUp = document.querySelector('.sign-up-button'),
      $btnGetIn = document.querySelector('.get-in');
const $btnGetOut = document.querySelector('.get-out');

      $signUp = document.querySelector('.sign-up'),
      $signIn = document.querySelector('.sign-in');
      $bahir = document.querySelector('.bahir')

document.addEventListener('click', e => {
    if (e.target === $btnSignIn  || e.target === $btnSignUp){
        window.location.replace("http://www.w3schools.com");
    }
});

document.addEventListener('click', e => {
    if (e.target === $btnGetOut  || e.target === $btnGetIn){
        $bahir.classList.toggle('active');
        $signIn.classList.toggle('active');  
    }
});
