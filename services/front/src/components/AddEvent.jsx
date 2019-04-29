import React from 'react';

    const AddEvent = (props) => {
    return (
        <div>
        {
             <div className="column is-one-third container is-fluid">
                <form onSubmit={(event) => props.addRecord(event)}>
                    <p><b> 小朋友的名字</b></p>
                    <div className="control">
                        <label className="radio">
                             <input name="userName" type="radio" value="不點"
                                    checked={props.userName === "不點" }
                                    onChange={props.handleChange}
                             />不點
                        </label>
                        <label className="radio">
                             <input name="userName" type="radio" value="頭妹"
                                    checked={props.userName === "頭妹" }
                                    onChange={props.handleChange}
                             />頭妹
                        </label>
                    </div>
                    <div className="field">
                        <label className="label">零用錢的數目</label>
                            <input
                                className="input"
                                name="money"
                                type="text"
                                placeholder="多少錢"
                                onChange={props.handleChange}
                            />
                    </div>
                    <div className="field">
                        <label className="label">因什麼事得到獎勵</label>
                            <input
                                className="input"
                                name="activities"
                                type="text"
                                placeholder="具體事蹟"
                                value={props.activities}
                                onChange={props.handleChange}
                            />
                    </div>
                    <div className="control">
                        <button className="button is-primary"> 確定送出 </button>
                    </div>
                </form>
            </div>
        }
        </div>
    )
    };

export default AddEvent;
