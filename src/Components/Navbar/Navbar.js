import React, {Component} from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
// import icon from './TJ.svg';


class Navbar extends Component {
    state = {


        AvatarInitails: ""
    }



    render() {

        return (
            <>
                <AppBar position="static" style={{
                    backgroundColor: "#1d2d50",
                    height: "50px",
                }}>
                    <Toolbar variant="dense" style={{
                        display: "flex",
                        justifyContent: "center",
                        alignItems: "center",
                        fontFamily: "'Roboto', sans-serif",
                        fontSize: "20px",
                        marginBottom: "-30px",
                        color: "#fcdab7"
                    }}>
                        {/*<img src={icon} width={40} alt="error"/>*/}
                        Google Play Store App Launch Study

                    </Toolbar>

                </AppBar>

            </>
        );
    }
}

// const mapStateToProps = state => {
//     console.log("APP JS STATE: ", state.token)
//     return {
//         isAuthenticated: state.token !== null,
//         isAdmin: state.admin_priority
//     }
// }


// const mapDispatchToProps = dispatch => {
//     return {
//         logout: () => dispatch(actions.logout())
//     }
// }
//
// export default connect(null, mapDispatchToProps)(Navbar);
export default Navbar;
