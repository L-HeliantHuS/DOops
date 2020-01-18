<template>
	<div>
		<head-top/>
		<div class="center">
			<el-form ref="form" :model="form" label-width="80px">
				<el-form-item label="组名称">
					<el-input v-model="form.group" placeholder="请输入组名称"/>
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
	import {APIAddGroup, APIAddHost} from "../api/api";

	export default {
		name: "GroupAddPage",
		components: {
			headTop
		},
		data() {
			return {
				form: {
					group: '',
				},
				loading: false,
			}
		},

		methods: {
			// 提交表单
			onSubmit() {
				this.loading = true;
				APIAddGroup(this.form).then(response => {
					if (response.code === 0) {
						this.$message({
							type: 'success',
							message: response.msg
						})
					} else {
						this.$message({
							type: 'error',
							message: response.msg
						});
					}

					this.loading = false;
					this.resetForm('form')
				})
			},

			// 清空表单
			resetForm() {
				this.form = {
					group: '',
				}
			}
		}
	}
</script>

<style scoped>

</style>
