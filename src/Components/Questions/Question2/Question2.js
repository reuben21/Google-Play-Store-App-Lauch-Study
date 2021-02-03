import React, {Component} from 'react';
import {Bar} from "react-chartjs-2";
import 'chart.piecelabel.js';

class Questions2 extends Component {
    state={
        key:[],
        value:[],
        colors:[]
    }
    componentDidMount() {
        fetch('http://127.0.0.1:5000/ques2', {
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
                    borderColor:'black',
                    barPercentage:0.5,
                    label:"No. Of Downloads"
                }
            ],
            labels: this.state.key,
        };
        let fontColor = 'red';
        const options = {

            title: {
                display: true,
            },

            legend: {
                display: true,
                position: 'bottom',
                fullWidth:true,
                labels: {
                    fontColor: '#fcdab7',
                    fontFamily: "'Roboto', sans-serif",
                },


            },
            scales: {
                yAxes: [{
                    gridLines: {
                        color: '#fcdab7'
                    },
                    ticks: {
                        beginAtZero:true,
                        fontColor: '#fcdab7',
                    },
                }],
                xAxes: [{
                    gridLines: {
                        color: '#fcdab7'
                    },
                    ticks: {
                        beginAtZero:true,
                        fontColor: '#fcdab7',
                    },
                }]
            }
        }
        return (<div style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            flexDirection: "column"

        }}>
            <h3>How many apps have managed to get the following number of downloads <br/>
                a) Between 10,000 and 50,000
                b) Between 50,000 and 150000
                c) Between 150000 and 500000
                d) Between 500000 and 5000000
                e) More than 5000000
            </h3>
            <div style={{
                marginTop:"40px",
                width: "80%",
                height:"100%"
            }}>
                <Bar data={data} options={options}/>


            </div>


        </div>)
    }
}

export default Questions2;
