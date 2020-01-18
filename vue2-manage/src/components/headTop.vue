<template>
	<div class="header_container">
		<el-breadcrumb separator="/">
			<el-breadcrumb-item :to="{ path: '/manage' }">首页</el-breadcrumb-item>
			<el-breadcrumb-item v-for="(item, index) in $route.meta" :key="index">{{item}}</el-breadcrumb-item>
		</el-breadcrumb>
		<el-dropdown @command="handleCommand" menu-align='start'>
			<img :src="baseImgPath + adminInfo.avatar" class="avator">
			<el-dropdown-menu slot="dropdown">
				<el-dropdown-item command="home">首页</el-dropdown-item>
				<el-dropdown-item command="signout">退出</el-dropdown-item>
			</el-dropdown-menu>
		</el-dropdown>
	</div>
</template>

<script>
	import {signout} from '@/api/getData'
	import {baseImgPath} from '@/config/env'
	import {mapActions, mapState} from 'vuex'
	import * as API from '../api/api'

	export default {
		data() {
			return {
				baseImgPath,
			}
		},
		created() {
			// 创建页面之前先看一下是否登录
			API.APIisLogin().then(response => {
				if (response.code !== 0) {
					this.$router.push('/');
					this.$message({
						type: 'warning',
						message: response.msg
					});
				}
			});


			if (!this.adminInfo.id) {
				this.getAdminData()
			}

		},
		computed: {
			...mapState(['adminInfo']),
		},
		methods: {
			...mapActions(['getAdminData']),
			async handleCommand(command) {
				if (command === 'home') {
					this.$router.push('/manage');
				} else if (command === 'signout') {
					// 直接请求注销API 不要返回值
					API.APILogout();
					this.$message({
						type: 'success',
						message: '退出成功'
					});
					this.$router.push('/');

				}
			},
		}
	}
</script>

<style lang="less">
	@import '../style/mixin';
	
	.header_container {
		background-color: #EFF2F7;
		height: 60px;
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding-left: 20px;
	}
	
	.avator {
		.wh(36px, 36px);
		border-radius: 50%;
		margin-right: 37px;
	}
	
	.el-dropdown-menu__item {
		text-align: center;
	}
</style>
