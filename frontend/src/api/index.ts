import axios from "axios";
import { Message, User, Inter } from "../types"

const makefunc = <Args, Out>(url: String) => {
    const API_URL = "http://127.0.0.1:8000/api/"; //TODO hardcoded for now
    const func = async (args?: Args) => {
        let api_url = API_URL + url;
        if (args) {
            api_url += "?"
            for (const [key, value] of Object.entries(args)) {
                if (value) {
                    api_url += `&${key}=${value}`
                }
            }
        }
        try {
            console.log(`calling ${api_url}`)
            const response = await axios.get(api_url);
            return response.data as Out; 
        } catch (error) {
            console.log(error)
        }
    }
    return func
}

// Message

export const getHistory = makefunc<null, Message[]>("message/history");
export const getUserMsg = makefunc<{ id: string }, Message[]>("message/usermsg");
export const getDateMsg = makefunc<{ mind?: string, maxd?: string }, Message[]>("message/datemsg");
export const getMsgInter = makefunc<{ id?: string }, Inter>("message/inter");
// export const getUserDate = makefunc("message/userdate");
// export const getMsgInfo = makefunc("message/msginfo");
// export const getMessage = makefunc("message");

// users
export const getUsers = makefunc<null, User[]>("user/users");
// export const getUser = makefunc("user/user");
// export const getUsers = makefunc("user");




