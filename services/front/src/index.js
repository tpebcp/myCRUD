import React, {Component} from "react"
import ReactDOM from 'react-dom';
import axios from 'axios'
import EventList from './components/EventList'
import AddEvent from './components/AddEvent'

class App extends Component {
    
    constructor() {
        super()
        this.state = {
            records: [],
            userName: "",
            money: "",
            activities: ""
        }
        this.addRecord = this.addRecord.bind(this); 
        this.handleChange = this.handleChange.bind(this)
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    getRecords() {  //  奇怪這支程式不用binding...
         // console.log(process.env.REACT_APP_USERS_SERVICE_URL)
         axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/events`)
         .then((res) => { 
             //console.log(res); 
             this.setState({ records: res.data.data.events }); 
         })
         .catch((err) => { console.log(err); });
    }

    addRecord(event) {
        event.preventDefault();
        console.log(this.state);
        const data = {
            username: this.state.userName,  // 極難除的錯：username全小寫，配合資料庫欄位全小寫
            activities: this.state.activities,
            money: this.state.money
        };
        axios.post(`${process.env.REACT_APP_USERS_SERVICE_URL}/events`, data)
        .then(
            (response) => {
            //console.log(response);
            this.getRecords();
            this.setState({userName:'',activities:'', money:''}); // 清空輸入欄，在寫入backend API之後
            }
        )
        .catch((error) => {console.log(error)})
    };

    componentDidMount() {
        this.getRecords();
    };

    render() {
        return (
            <div className="columns">
                <div className="column container is-fluid">
                    <AddEvent 
                        userName={this.state.userName}              // 傳值
                        activities={this.state.activities}          // 傳值
                        money={this.state.money}                    // 傳值
                        addRecord={this.addRecord}                    // 傳，或說呼叫function addUser
                        handleChange={this.handleChange}            // 傳，或說呼叫function handleChange
                    />
                    <h1>{this.state.userName} {this.state.money} {this.state.activities}</h1> 
                </div>
                <div className="column container is-fluid">
                    <h4> 過往紀錄 </h4>
                    <div className="box title is-4">
                        <EventList record={this.state.records}/>
                    </div>
                </div>
            </div>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('root'));
