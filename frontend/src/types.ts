
export interface Message {
    message_id: number;
    author_id: number;
    content: string;
    date: string;
}

export interface User {
    avatar_url: string
    name: string
    discriminator: string
    user_id: string
    ghost: boolean
    nb_msg: number
    top: number
}

export type Inter = [string, Message[]][]