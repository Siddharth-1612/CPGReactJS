import React, { useState } from 'react';

function InterestCalculator() {
    const [principal, setPrincipal] = useState('');
    const [rate, setRate] = useState('');
    const [time, setTime] = useState('');
    const [interestType, setInterestType] = useState('simple'); // Default to Simple Interest
    const [result, setResult] = useState(null);

    const calcInterest = () => {
        let p = parseFloat(principal);
        let r = parseFloat(rate);
        let t = parseFloat(time);

        if (isNaN(p) || isNaN(r) || isNaN(t)) {
            setResult("Please enter valid numbers");
            return;
        }

        let interest = 0;
        if (interestType === 'simple') {
            interest = (p * r * t) / 100; // Simple Interest formula
        } else {
            interest = p * Math.pow(1 + r / 100, t) - p; // Compound Interest formula
        }

        setResult(interest.toFixed(2)); // Display result up to 2 decimal places
    };

    return (
        <div style={styles.container}>
            <h2>Interest Calculator</h2>

            <label>Principal (P):</label>
            <input
                type="number"
                value={principal}
                onChange={(e) => setPrincipal(e.target.value)}
                style={styles.input}
                placeholder="Enter principal amount"
            />

            <label>Rate of Interest (R% per year):</label>
            <input
                type="number"
                value={rate}
                onChange={(e) => setRate(e.target.value)}
                style={styles.input}
                placeholder="Enter rate of interest"
            />

            <label>Time (T in years):</label>
            <input
                type="number"
                value={time}
                onChange={(e) => setTime(e.target.value)}
                style={styles.input}
                placeholder="Enter time in years"
            />

            <label>Select Interest Type:</label>
            <select
                value={interestType}
                onChange={(e) => setInterestType(e.target.value)}
                style={styles.select}
            >
                <option value="simple">Simple Interest</option>
                <option value="compound">Compound Interest</option>
            </select>

            <button onClick={calcInterest} style={styles.button}>
                Calculate Interest
            </button>

            {result !== null && <h3>Interest: {result}</h3>}
        </div>
    );
}

const styles = {
    container: {
        textAlign: "center",
        maxWidth: "400px",
        margin: "auto",
        padding: "20px",
        border: "1px solid #ccc",
        borderRadius: "10px",
        backgroundColor: "#f9f9f9",
        boxShadow: "0px 0px 10px rgba(0,0,0,0.1)",
    },
    input: {
        display: "block",
        width: "90%",
        margin: "10px auto",
        padding: "8px",
        fontSize: "16px",
    },
    select: {
        display: "block",
        width: "95%",
        margin: "10px auto",
        padding: "8px",
        fontSize: "16px",
    },
    button: {
        padding: "10px 20px",
        fontSize: "16px",
        backgroundColor: "#007BFF",
        color: "white",
        border: "none",
        borderRadius: "5px",
        cursor: "pointer",
    },
};

export default InterestCalculator;
