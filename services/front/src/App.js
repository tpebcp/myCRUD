import React, {Component} from "react"

class App extends Component {
    constructor() {
        super()
        this.state = {
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

    render() {
        return (
            <div class="columns">
                <div class="column is-one-third container is-fluid">
                <form>
                    <p><b> 小朋友的名字</b></p>
                    <div class="control">
                        <label class="radio">
                             <input name="userName" type="radio" value="不點"
                                    checked={this.state.userName === "不點" } 
                                    onChange={this.handleChange}
                             />不點
                        </label>
                        <label class="radio">
                             <input name="userName" type="radio" value="頭妹"
                                    checked={this.state.userName === "頭妹" } 
                                    onChange={this.handleChange} 
                             />頭妹
                        </label>
                    </div>
                    <div class="field">
                        <label class="label">零用錢的數目</label>
                            <input 
                                class="input" 
                                name="money"
                                type="text" 
                                placeholder="多少錢"
                                onChange={this.handleChange}
                            />
                    </div>
                    <div class="field">
                        <label class="label">因什麼事得到獎勵</label>
                            <input 
                                class="input" 
                                name="event"
                                type="text" 
                                placeholder="具體事蹟"
                                onChange={this.handleChange}
                            />
                    </div>
                    <div class="control">
                        <button class="button is-primary"> 確定送出 </button>
                    </div>
                </form>
            </div>
        <h1>{this.state.userName} {this.state.money} {this.state.event} </h1> 
            </div>
        )
    }
}

export default App
