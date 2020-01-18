<template>
	<div>
		<head-top/>
		<div class="center">
			<el-form ref="form" :model="form" label-width="80px">
				<el-form-item label="主机描述">
					<el-input v-model="form.remark" placeholder="请输入描述"/>
				</el-form-item>
				<el-form-item label="选择分组">
					<el-select v-model="form.group" placeholder="请选择活动区域">
						<el-option
								v-for="item in gorups"
								:key="item.id"
								:value="item.id"
								:label="item.group_name"
						/>
					</el-select>
				</el-form-item>
				
				<el-form-item label="主机地址">
					<el-input v-model="form.hostname" placeholder="主机IP地址"/>
				</el-form-item>
				
				<el-form-item label="端口">
					<el-input-number v-model="form.port"/>
				</el-form-item>
				
				<el-form-item label="用户名">
					<el-input v-model="form.username" placeholder="主机SSH用户名"/>
				</el-form-item>
				
				<el-form-item label="密码">
					<el-input type="password" v-model="form.password" placeholder="主机SSH密码, 使用公钥连接可以不用填写"/>
				</el-form-item>
				
				
				<el-form-item>
					<el-button type="primary" @click="onSubmit" :loading="loading">立即创建</el-button>
					<el-button @click="resetForm">重置</el-button>
				</el-form-item>
			</el-form>
		</div>
	</div>
</template>

<script>
	import headTop from "../components/headTop";
	import {APIAddHost, APIGetGroups} from "../api/api";

	export default {
		name: "HostAddPage",
		components: {
			headTop
		},
		data() {
			return {
				gorups: [],  // 存放分组名称
				form: {
					remark: '',
					group: null,
					hostname: '',
					port: 22,
					username: '',
					password: '',
				},
				loading: false,

			}
		},
		created() {
			this.getGroup();


		},
		methods: {
			// 获得所有分组 用来选择
			async getGroup() {
				APIGetGroups().then(response => {
					if (response.code === 0) {
						this.gorups = response.data
					}
				})
			},

			// 提交表单
			onSubmit() {
				this.loading = true;
				APIAddHost(this.form).then(response => {
					if (response.code === 0) {
						this.$message({
							type: 'success',
							message: response.msg
						})
					}
					this.$message({
						type: 'error',
						message: response.msg
					});
					
					this.loading = false;
				})
			},
			
			// 清空表单
			resetForm() {
				this.form = {
					remark: '',
					group: null,
					hostname: '',
					port: 22,
					username: '',
					password: '',
				}
			}

		}

	}
</script>

<style scoped>

</style>
