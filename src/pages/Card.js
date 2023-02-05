import { useNavigate } from 'react-router-dom';
import '../Card.css'
import logo from '../anonymous.png'
import React, { useState } from 'react'

let count = 0;

function Card(props) {
    const [count, setCount] = useState(0)
    const [rightButton, setrightButton] = useState(false)
    console.log(props["data"])
    const navigate = useNavigate()

    if (rightButton == true && props?.data?.length != 0) {
        function myName() {
            const a = setTimeout(myAlert);
        }

        function myAlert() {
            alert('Call ' + props["data"][0][2] + ' to get in contact with them!', 1000);

        }
        myName()
    }
    if (count == props?.data?.length) {
        return (
            <div className="end-website">
                <h1>Sorry, no matches were found.</h1>
                <button className="last-page-button" onClick={() => navigate('/')}>Click here to go back and try another location!</button>
            </div>
        )
    }

    return (
        <div className="card">
            <div className="card-holder">
                <h1 className="title-card-page">Find Your Match!</h1>
                <div className="card_body">
                    <img className="picture" src={logo} />
                    <h1 className="card_name">{props["data"][count][0]}</h1>
                    <h2 className="card_title">{props["data"][count][1]}</h2>
                    <p className="card_year">{props["data"][count][3]}</p>
                </div>
                <div className="card-bottom-container">
                    <button onClick={() => setCount(count + 1)} className="left-button">Nah!</button>
                    <button onClick={() => setrightButton(true)} className="right-button">Yeah!</button>
                </div>
            </div>

        </div>
    )
}


export default Card;