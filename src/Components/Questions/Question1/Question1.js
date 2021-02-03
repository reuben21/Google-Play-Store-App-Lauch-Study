import React, {Component} from 'react';
import {Pie} from "react-chartjs-2";
import 'chart.piecelabel.js';

class Questions1 extends Component {
    state={
        key:[],
        value:[],
        colors:[]
    }
    componentDidMount() {
        fetch('http://127.0.0.1:5000/ques1', {
            method: 'GET',
            // headers: {
            //     'Content-Type': 'application/json'
            //     // 'Content-Type': 'application/x-www-form-urlencoded',
            // },
        })
            .then(resp => resp.json())
            .then(data => {
                console.log(data)
                this.setState({
                    key:data.labels,
                    value:data.values,
                    colors:data.colors

                })
                return data;
            }).catch((error) => {
            return error;
        })
    }

    render() {
        const data = {

            datasets: [
                {

                    backgroundColor:this.state.colors,
                    data: this.state.value,
                    borderColor:'transparent'
                }
            ],
            labels: this.state.key,
        };
        const options = {
            pieceLabel: {
                render: 'value',
                fontColor: 'black',
            },
            title: {
                display: false,
            },
            rotation: Math.PI,
            cutoutPercentage: 0,
            legend: {
                display: true,
                position: 'bottom',
                fullWidth:true,
                labels: {
                    fontColor: '#fcdab7',
                    fontFamily: "'Roboto', sans-serif",
                },
                hidden:true

            },
            tooltip:{
                enabled: true,
            }
        }
        return (<div style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            flexDirection: "column"

        }}>
            <h1>What is the percentage download in each category on the play store.</h1>
            <div style={{
                marginTop:"40px",
                width: "80%",
                height:"100%"
            }}>
                <Pie data={data} options={options}/>


            </div>


        </div>)
    }
}

export default Questions1;
