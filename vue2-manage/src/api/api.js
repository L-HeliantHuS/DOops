import axios from 'axios'

// Use:
// import * as API from '../api/api'

// 登录API
const APILogin = (form) => {
	return axios.post("/api/user/login", form).then(response => response.data)
};

// 注销API
const APILogout = () => {
	return axios.get("/api/user/logout").then(response => response.data)
};

// 判断是否登录API
const APIisLogin = () => {
	return axios.get("/api/user/isLogin").then(response => response.data)
};

// 主页返回主机状态
const APIHostStatus = () => {
	return axios.get("/api/status").then(response => response.data)
};

// 获取所有主机
const APIGetHosts = () => {
	return axios.get("/api/host").then(response => response.data)
};

// 获取所有组
const APIGetGroups = () => {
	return axios.get("/api/group").then(response => response.data)
};

// 添加主机
const APIAddHost = (form) => {
	return axios.post("/api/host", form).then(response => response.data)
};

// 添加组
const APIAddGroup = (form) => {
	return axios.post("/api/group", form).then(response => response.data)
};

export {
	APILogin,
	APILogout,
	APIisLogin,
	APIHostStatus,
	APIGetGroups,
	APIAddHost,
	APIAddGroup,
	APIGetHosts
}




