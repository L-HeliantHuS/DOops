<template>
	<div>
		<head-top></head-top>
		<section class="data_section">
			<header class="section_title">数据统计</header>
			<el-row :gutter="20" style="margin-bottom: 10px;">
				<el-col :span="12">
					<el-card shadow="hover">
						<i class="el-icon-setting"></i>
						当前主机个数：{{ hosts_count }}
					</el-card>
				</el-col>
				<el-col :span="12">
					<el-card shadow="hover">
						<i class="el-icon-setting"></i>
						当前用户数：{{ users_count }}
					</el-card>
				</el-col>
				<!--				<el-col :span="4"><div class="data_list"><span class="data_num">{{userCount}}</span> 新增用户</div></el-col>-->
				<!--				<el-col :span="4"><div class="data_list"><span class="data_num">{{orderCount}}</span> 新增订单</div></el-col>-->
				<!--                <el-col :span="4"><div class="data_list"><span class="data_num">{{adminCount}}</span> 新增管理员</div></el-col>-->
			</el-row>
			<!--            <el-row :gutter="20">-->
			<!--                <el-col :span="4"><div class="data_list all_head"><span class="data_num head">总数据：</span></div></el-col>-->
			<!--                <el-col :span="4"><div class="data_list"><span class="data_num">{{allUserCount}}</span> 注册用户</div></el-col>-->
			<!--                <el-col :span="4"><div class="data_list"><span class="data_num">{{allOrderCount}}</span> 订单</div></el-col>-->
			<!--                <el-col :span="4"><div class="data_list"><span class="data_num">{{allAdminCount}}</span> 管理员</div></el-col>-->
			<!--            </el-row>-->
		</section>
		<!--		<tendency :sevenDate='sevenDate' :sevenDay='sevenDay'></tendency>-->
	</div>
</template>

<script>
	import headTop from '../components/headTop'
	import tendency from '../components/tendency'
	import * as API from '../api/api'

	export default {
		data() {
			return {
				hosts_count: 0,
				users_count: 0

			}
		},
		components: {
			headTop,
			tendency,
		},
		mounted() {
			// 初始化数据
			this.initData();
			
		},
		computed: {},
		methods: {
			async initData() {
				API.APIHostStatus().then(response => {
					if (response.code === 0) {
						this.hosts_count = response.data.hosts_count;
						this.users_count = response.data.users_count
					}

				})
			}
		}
	}
</script>

<style lang="less">
	@import '../style/mixin';
	
	.data_section {
		padding: 20px;
		margin-bottom: 40px;
		
		.section_title {
			text-align: center;
			font-size: 30px;
			margin-bottom: 10px;
		}
		
		.data_list {
			text-align: center;
			font-size: 14px;
			color: #666;
			border-radius: 6px;
			background: #E5E9F2;
			
			.data_num {
				color: #333;
				font-size: 26px;
				
			}
			
			.head {
				border-radius: 6px;
				font-size: 22px;
				padding: 4px 0;
				color: #fff;
				display: inline-block;
			}
		}
		
		.today_head {
			background: #FF9800;
		}
		
		.all_head {
			background: #20A0FF;
		}
	}
	
	.wan {
		.sc(16px, #333)
	}
</style>
