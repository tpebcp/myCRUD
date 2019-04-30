import React from 'react';
// 傳進來的props是物件，一包，裏頭再分幾個item
// 但不可思議的是item不用定義就可叫用
    const EventList = (props) => {
        return (
            <div>
                <h4 key={props.item.id} className={ props.item.disabled? "has-text-grey-light":"has-text-black" } >
                    <input 
                         type="checkbox" 
                         checked={props.disabled}
                         onChange={ () => { props.handleClick(props.item.id) } }
                    />
                    { 
                       props.item.username 
                    } 
                    { 
                       props.item.activities 
                    }
                    { 
                       props.item.money 
                    }
                 </h4>
            </div>
        )
    };

export default EventList;
