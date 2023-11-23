// index.js
// const app = getApp()
const { envList } = require('../../envList.js');

Page({
  clickMe:function(){
    this.setData({msg:"你好世界"})
  },

  tapName: function(event) { 
    console.log(event) 
  },
  data: {
    true_or_false:false,
    money_left:20,
    ayi_work:true,
    percent:50,
    // name_list:[{
    //   title='注意事项',
    //   showitem=false,
    //   item:[{
    //   title="小心不要摔坏任何物品"
    //   }]
    // }],
    showUploadTip: false,
    powerList: [{
      title: '未完成',
      tip:'需要抓紧时间完成',
      showItem: false,
      item: [{
        title: '清理拖鞋',
      },
      //  {
      //   title: '微信支付'
      // },
       {
        title: '第二次清洁地面',
        // showItem:true,
        // item:[{
        //   title:"13:00"
        // }]
      },
       {
        title:"擦洗冰箱（客厅和B1）"
      },
      {
        title:"全屋墙面和玻璃镜面清洁"
      }
      // {
      //   title: '发送订阅消息',
      // }
    ]
    }, {
      title:'家里人',
      showItem:false,
      item:[{
        title:'妈妈',
      },{
        title:'爸爸',
      },{
        title:'姥姥',
      },{
        title:'姥爷',
      }]
    },{
      title: '已完成',
      tip: '继续保持',
      showItem: false,
      item: [{
        title: '卫生间清洁B1和B2',
      }, 
      {
        title: '三层到B2所有清洁',
      }
    ]
    }],
    envList,
    selectedEnv: envList[0],
    haveCreateCollection: false
  },

  onClickPowerInfo(e) {
    const index = e.currentTarget.dataset.index;
    const powerList = this.data.powerList;
    powerList[index].showItem = !powerList[index].showItem;
    if (powerList[index].title === '数据库' && !this.data.haveCreateCollection) {
      this.onClickDatabase(powerList);
    } else {
      this.setData({
        powerList
      });
    }
  },

  onChangeShowEnvChoose() {
    wx.showActionSheet({
      itemList: this.data.envList.map(i => i.alias),
      success: (res) => {
        this.onChangeSelectedEnv(res.tapIndex);
      },
      fail (res) {
        console.log(res.errMsg);
      }
    });
  },

  onChangeSelectedEnv(index) {
    if (this.data.selectedEnv.envId === this.data.envList[index].envId) {
      return;
    }
    const powerList = this.data.powerList;
    powerList.forEach(i => {
      i.showItem = false;
    });
    this.setData({
      selectedEnv: this.data.envList[index],
      powerList,
      haveCreateCollection: false
    });
  },

  jumpPage(e) {
    wx.navigateTo({
      url: `/pages/${e.currentTarget.dataset.page}/index?envId=${this.data.selectedEnv.envId}`,
    });
  },

  onClickDatabase(powerList) {
    wx.showLoading({
      title: '',
    });
    wx.cloud.callFunction({
      name: 'quickstartFunctions',
      config: {
        env: this.data.selectedEnv.envId
      },
      data: {
        type: 'createCollection'
      }
    }).then((resp) => {
      if (resp.result.success) {
        this.setData({
          haveCreateCollection: true
        });
      }
      this.setData({
        powerList
      });
      wx.hideLoading();
    }).catch((e) => {
      console.log(e);
      this.setData({
        showUploadTip: true
      });
      wx.hideLoading();
    });
  }
});
