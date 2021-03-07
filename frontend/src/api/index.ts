import axios from "axios";

const makefunc = (url:String) => {
    const API_URL = "http://127.0.0.1:8000/api/"; //TODO hardcoded for now
    const func = async (args?:{id?:String, mind?:String, maxd?:String, info?:String})=>{
        let api_url = API_URL + url;
        if (args){
            const {id,mind,maxd,info}=args;
            api_url += "?"
            if (id){
                api_url += `id=${id}&`
            }
            if (mind){
                api_url += `mind=${mind}`
            }
            if (maxd){
                api_url += `maxd=${maxd}`
            }
            if (info){
                api_url += `info=${info}`
            }
        }
        try {
            const response = await axios.get(api_url);
            return response.data; // TODO find a way to type this 
        } catch (error) {
            
        }
    }
    return func
}

// Message

export const getHistory  = makefunc("message/history");
export const getUserMsg  = makefunc("message/usermsg");
export const getDateMsg  = makefunc("message/datemsg");
export const getUserDate = makefunc("message/userdate");
export const getMsgInfo  = makefunc("message/msginfo");
export const getMessage  = makefunc("message");

// users
export const getAllUsers = makefunc("user/users");
export const getUser     = makefunc("user/users");
export const getUsers    = makefunc("user");

// count data
export const getCount    = makefunc("count");


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
    id:String 

}

interface Users{
    String:User
}
