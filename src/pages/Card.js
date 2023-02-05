import React from 'react'
import '../Card.css'


function Card(props) {
    return (
        <div className="card">
            <div className="card__body">
                <img className="card__img" src={props.img} />
                <h2 className="card__title">{props.title}</h2>
                <p className="card__description">{props.description}</p>
            </div>
            <button className="card__btn">View Info</button>

        </div>
    )
}


export default Card;