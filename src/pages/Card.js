import { navigate, useNavigate } from 'react-router-dom';
import '../Card.css'
import logo from '../anonymous.png'
import React, { useState } from 'react'

let count = 0;

function Card(props) {
    const [count, setCount] = useState(0)
    console.log(props["data"])


    if (count == props?.data?.length) {
        return (
            <div className="end-website">
                <h1>Sorry. No matches were found.</h1>
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
                    <p className="card__number">{props["data"][count][2]}</p>
                    <p className="card_year">{props["data"][count][3]}</p>
                </div>
                <div className="card-bottom-container">
                    <button onClick={() => setCount(count + 1)} className="left-button">Nah!</button>
                    <button className="right-button">Yeah!</button>
                </div>
            </div>

        </div>
    )
}


export default Card;