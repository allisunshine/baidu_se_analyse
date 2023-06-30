import React, {useState, useEffect} from 'react';
import {Table, Pagination, Input, Tooltip} from 'antd';
import {render} from 'react-dom';

const {Search} = Input;

const fetchData = async (word, page, pageSize) => {

    try {
        const response = await fetch('/baike/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                word,
                page,
                pageSize,
            }),
        });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        return null;
    }
};


const SearcePage = () => {
    const [data, setData] = useState([]);
    const [total, setTotal] = useState(0);
    const [currentPage, setCurrentPage] = useState(1);
    const [pageSize, setPageSize] = useState(10);
    const [searchWord, setSearchWord] = useState('');

    console.log('SearcePage')
    useEffect(() => {
        // 在组件加载时调用查询函数，默认获取第一页数据
        fetchData('', 1, pageSize).then((searchData) => {
            if (searchData) {
                setData(searchData.results);
                setTotal(searchData.total_count);
            }
        });
    }, []);

    const handleSearch = async () => {
        setCurrentPage(1); // Reset current page when performing a new search
        const searchData = await fetchData(searchWord, 1, pageSize);
        if (searchData) {
            setData(searchData.results);
            setTotal(searchData.total_count);
        }
    };

    const handlePageChange = async (page, pageSize) => {
        setCurrentPage(page);
        const searchData = await fetchData(searchWord, page, pageSize);
        if (searchData) {
            setData(searchData.results);
        }
    };

    const handlePageSizeChange = async (current, size) => {
        setCurrentPage(1);
        setPageSize(size);
        const searchData = await fetchData(searchWord, 1, size);
        if (searchData) {
            setData(searchData.results);
            setTotal(searchData.total_count);
        }
    };

    const columns = [
        {title: 'ID', dataIndex: 'id', key: 'id'},
        {title: '网页编号', dataIndex: 'page_number', key: 'page_number'},
        {
            title: '关键字', dataIndex: 'keyword', key: 'keyword',
            width: 100,
             ellipsis:true,
            render: (text, record) => {
                console.log(text)
                return <Tooltip title={text}>
                    {text}
                </Tooltip>
            }

        },
        {title: '爬取关键词', dataIndex: 'search_word', key: 'search_word'},
        {title: '标题', dataIndex: 'title', key: 'title'},
        {title: '当前链接', dataIndex: 'current_url', key: 'current_url'},
        {title: '父链接', dataIndex: 'parent_url', key: 'parent_url'},
        {
            title: 'HTML主体内容', dataIndex: 'text_html', key: 'text_html',
            width: 100,
            ellipsis:true,
            render: (text, record) => {
                return <Tooltip title={text}>
                    {text}
                </Tooltip>
            }
        },
        {title: '创建时间', dataIndex: 'create_time', key: 'create_time'},
    ];
    console.log('hhhh')
    return (
        <div>
            < Search
                placeholder="Enter keyword"
                allowClear
                enterButton="Search"
                onSearch={handleSearch}
                onChange={(e) => setSearchWord(e.target.value)}
                style={{marginBottom: 16}}
            />
            <Table
                size={'small'}

                columns={columns} dataSource={data} pagination={false}/>
            <Pagination
                current={currentPage}
                pageSize={pageSize}
                total={total}
                showSizeChanger
                onChange={handlePageChange}
                onShowSizeChange={handlePageSizeChange}
                style={{marginTop: 16, textAlign: 'right'}}
            />
        </div>
    );
};

render(<SearcePage/>, document.getElementById('searchPages'))


// export default SearcePage;
