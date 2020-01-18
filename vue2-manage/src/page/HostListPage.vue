<template>
	<div>
		<head-top></head-top>
		<div class="center">
			<el-table :data="hosts" style="width: 1200px">
				<el-table-column
						prop="id"
						label="序号"
						width="180">
				</el-table-column>
				<el-table-column
						prop="remark"
						label="描述"
						width="180">
				</el-table-column>
				<el-table-column
						prop="hostname"
						label="主机IP"
						width="180">
				</el-table-column>
				
				<el-table-column
						prop="port"
						label="端口"
						width="180">
				</el-table-column>
				
				
				<el-table-column
						prop="username"
						label="用户名"
						width="180">
				</el-table-column>
				<el-table-column label="操作">
					<template slot-scope="scope">
						<el-button
								size="mini"
								@click="editHost(scope.row.id)"
						>编辑
						</el-button>
						<el-button
								size="mini"
								type="danger"
								@click="deleteHost(scope.row.id)"
						>删除
						</el-button>
					</template>
				</el-table-column>
			</el-table>
		</div>
	</div>
</template>

<script>
	import headTop from '../components/headTop'
	import * as API from '../api/api'

	export default {
		name: "HostListPage",
		components: {
			headTop
		},
		data() {
			return {
				hosts: []
			}
		},
		created() {
			this.getHosts()

		},


		methods: {
			// 获取全部主机
			getHosts() {
				API.APIGetHosts().then(response => {
					if (response.code === 0) {
						this.hosts = response.data;
					} else {
						this.$message({
							type: 'warning',
							message: response.msg
						})
					}
				})
			},
			
			// 删除一个主机
			deleteHost(id) {
				console.log("Delete ID:" + id)
			},
			
			
			editHost(id) {
				console.log("Edit ID:" + id)
			},
		}
	}
</script>

<style scoped>

</style>
