// import axios from "axios";
export const { count, last_update, podium } = require("./data/count") as Count;
export const history = require("./data/history") as Message[];
export const users = require("./data/users") as Users;

interface Count{
    last_update:number[];
    podium:{
        top1:String;
        top2:String;
        top3:String;
    };
    count:{
        String:number
    }
}

interface Message{
    message_id:number;
    author_id:number;
    content:String;
    date: number[];

}

interface User{
    avatar_url:String
    name:String
    discriminator:String
    id:number // TODO change this to String later

}

interface Users{
    String:User
}


// const url = window.location.href;

// export const fetchCount = async () => {
//   try {
//     const response = await axios.get(url+"/api/count");
//     return response;
//   } catch (error) {}
// };
