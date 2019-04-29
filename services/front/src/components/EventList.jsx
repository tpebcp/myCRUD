import React from 'react';

    const EventList = (props) => {
    return (
        <div>
        {
            props.record.map(
                (record) => {
            console.log(record)
                    return (
                        <h4 key={record.id} className="box title is-4">
                            { record.username}{ record.event}{record.money }
                        </h4>
                    )
            })
        }
        </div>
    )
    };

export default EventList;
