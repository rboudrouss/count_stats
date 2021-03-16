import React, { useState, useEffect } from "react";
import { Line } from "react-chartjs-2";

import styles from "./Chart.module.css";
import { getMsgInter } from "../../api";

const Chart = (props: any) => {
  const [data, setData] = useState([]);

  const selectedUser: String = props.selectedUser;

  useEffect(() => {
    const fetchAPI = async () => {
      const data1 = await getMsgInter({
        // max: 10,
        empty: false,
        id: selectedUser,
      });
      if (data1) {
        setData(data1);
      }
    };

    fetchAPI();
  }, [selectedUser]); // disabled autoupdate

  const lineChart = data ? (
    <Line
      data={{
        labels: data?.map((item) => item[0]),
        datasets: [
          {
            data: data?.map((item) => item[1]),
            label: "messages",
            borderColor: "#3333ff",
            fill: true,
          },
        ],
      }}
    />
  ) : (
    <Line
      data={{
        labels: [],
        datasets: [
          {
            data: 0,
            label: "User not Found",
            borderColor: "#ff0000",
            fill: true,
          },
        ],
      }}
    />
  );

  return <div className={styles.container}>{lineChart}</div>;
};

export default Chart;
