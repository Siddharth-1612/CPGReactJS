import React from 'react';

function Body(){
    return(
        <main style={styles.main}>
        <p> This is a simple react application with a structured layout</p>
    </main>
    );
}
const styles = {
    main: {
        backgroundColor: "#333",
        color: "white",
        padding: "10px",
        textAlign: "center",
    },
    
};

export default Body;