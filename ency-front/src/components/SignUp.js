import './css/SignUp.css';

function SignUpLayout() {
  return(
    <div className="layout">
      <form method="post" action="Signup function">
        <label htmlFor="email">Email:</label><br />
        <input type="text" placeholder="example@domain.com"></input><br /><br />
        <label htmlFor="name">Name:</label><br />
        <input type="text" placeholder="Preferred User Name"></input><br /><br />
        <label htmlFor="password">Password:</label><br />
        <input type="text" placeholder="Strong Password"></input><br /><br />
        <input type="submit"></input>
      </form>
    </div>      
  );
}

export default SignUpLayout;
