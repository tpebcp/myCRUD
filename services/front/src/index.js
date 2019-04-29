import React, {Component} from "react"
import ReactDOM from 'react-dom';
import axios from 'axios'
import EventList from './components/EventList'

class App extends Component {
    constructor() {
        super()
        this.state = {
            records: [],
            userName: "",
            money: "",
            event: ""
        }
        this.handleChange = this.handleChange.bind(this)
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    getRecords() {
         console.log(process.env.REACT_APP_USERS_SERVICE_URL)
         axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/events`)
         .then((res) => { this.setState({ records: res.data.data.events }); })
         .catch((err) => { console.log(err); });
    }

    componentDidMount() {
        this.getRecords();
    };

    render() {
        return (
            <div className="columns">
                <div className="column is-one-third container is-fluid">
                <form>
                    <p><b> 小朋友的名字</b></p>
                    <div className="control">
                        <label className="radio">
                             <input name="userName" type="radio" value="不點"
                                    checked={this.state.userName === "不點" } 
                                    onChange={this.handleChange}
                             />不點
                        </label>
                        <label className="radio">
                             <input name="userName" type="radio" value="頭妹"
                                    checked={this.state.userName === "頭妹" } 
                                    onChange={this.handleChange} 
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
                                onChange={this.handleChange}
                            />
                    </div>
                    <div className="field">
                        <label className="label">因什麼事得到獎勵</label>
                            <input 
                                className="input" 
                                name="event"
                                type="text" 
                                placeholder="具體事蹟"
                                onChange={this.handleChange}
                            />
                    </div>
                    <div className="control">
                        <button className="button is-primary"> 確定送出 </button>
                    </div>
                </form>
            </div>
            <div className="column is-one-third container is-fluid">
            <h1>{this.state.userName} {this.state.money} {this.state.event} </h1> 
            <EventList record={this.state.records}/>
            </div>
            </div>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('root'));
