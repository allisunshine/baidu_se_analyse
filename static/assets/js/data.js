var currentPage = 1;
var pageSize = 10;
$(document).ready(function () {
    // 监听表单提交事件
    $("#searchForm").submit(function (event) {
        event.preventDefault(); // 阻止表单默认提交行为

        var word = $("#searchInput").val(); // 获取输入框的值

        // 发起 AJAX 请求到后端接口
        $.ajax({
            url: "/baike/data",
            method: "POST",
            contentType: "application/json",
            data: JSON.stringify({word: word}),
            success: function (data) {
                // 处理后端返回的数据
                displayResults(data);
            },
            error: function (xhr, status, error) {
                console.log("请求出错:", error);
            }
        });
    });
});

function displayResults(data) {
    var tableHTML = "<table class='table result-table'><thead><tr><th>网页编号</th><th>关键字</th><th>爬取关键词</th><th>标题</th><th>当前链接</th><th>父链接</th><th>HTML主体内容</th><th>创建时间</th></tr></thead><tbody>";

    // 根据后端返回的数据构建表格内容
    for (var i = 0; i < data.length; i++) {
        var rowData = data[i];
        tableHTML += "<tr><td>" + rowData.page_number + "</td><td>" + rowData.keyword + "</td><td>" + rowData.search_word + "</td><td>" + rowData.title + "</td><td>" + rowData.current_url + "</td><td>" + rowData.parent_url + "</td><td class='overflow-ellipsis tooltip'><span class='tooltiptext'>" + rowData.text_html + "</span>" + rowData.text_html + "</td><td>" + rowData.create_time + "</td></tr>";
    }
    tableHTML += "</tbody></table>";

    $("#resultTable").html(tableHTML); // 在指定的元素中展示结果
}
