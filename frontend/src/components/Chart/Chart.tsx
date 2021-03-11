import React, { useState, useEffect } from "react";
import { Line } from "react-chartjs-2";

import styles from "./Chart.module.css";
import { getMsgInter } from "../../api";


const Chart = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchAPI = async () => {
      setData(await getMsgInter());
    };
    console.log(data);

    fetchAPI();
  });

  const lineChart = data ? (
    <Line
      data={{
        labels: data?.map((item)=>item[0]),
        datasets: [{
          data:data?.map((item)=>item[1]),
          label:"messages",
          borderColor:"#3333ff",
          fill:true
        }],
      }}
    />
  ) : null;

  return (
    <div className={styles.container}>
      {lineChart}
    </div>
  );
};

export default Chart;
