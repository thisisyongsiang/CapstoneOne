import pytest
import json
import CategoryAndFilter as ct
import Heapsort
import MergeSort
import QuickSelect


@pytest.fixture
def data():
    dir="singaporeFnBAll.json"
    f=open(dir,encoding='utf-8')
    data=json.load(f)

    # Get Base Data to display first
    clean_data = ct.simplifyData(data, [1.397427, 103.881539], 1, 2, 3)
    return clean_data


# simplifyData returns correct results
def test_case_1(data):
    assert len(data) == 54259   # 54753 total data points, 494 data points skipped due lack of 'latitude' field
    assert data[0]['name'] == 'Spageddies'  # First item
    assert data[54258]['name'] == 'Spice Junction'  # Last item
    assert data[0]['distance'] == 16931.679249607503


# Filter data by field and value range
def test_case_2(data):
    clean_data = ct.filterDataByFieldAndValueRange(data, 'distance', [0, 40000])
    assert len(clean_data) == 54259
    clean_data = ct.filterDataByFieldAndValueRange(data, 'distance', [0, 1000])
    assert len(clean_data) == 175

    clean_data = ct.filterDataByFieldAndValueRange(data, 'price', [0, 4])
    assert len(clean_data) == 54259
    clean_data = ct.filterDataByFieldAndValueRange(data, 'price', [3, 4])
    assert len(clean_data) == 1839


# Heapsort
def test_case_3(data):
    temp_data = Heapsort.getItemsByField(data, 'distance', True)
    assert len(temp_data.arr) == 54259
    clean_data = temp_data.getNextN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Michin Korean Bbq & Hotpot'    # Top shortest distance
    assert clean_data[4]['name'] == 'Mushroom Cafe'

    clean_data = temp_data.getNextN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Mushroom Cafe' 
    assert clean_data[4]['name'] == 'Essen, the Anchorvale'

    clean_data = temp_data.getPrevN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Michin Korean Bbq & Hotpot' 
    assert clean_data[4]['name'] == 'Mushroom Cafe'

    temp_data = Heapsort.getItemsByField(data, 'recommendation', False)
    assert len(temp_data.arr) == 54259
    clean_data = temp_data.getNextN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Nylon Coffee Roasters'     # Top Recommendation score
    assert clean_data[4]['name'] == 'Ps.Cafe'

    temp_data = Heapsort.getItemsByField(data, 'price', False)
    assert len(temp_data.arr) == 54259
    clean_data = temp_data.getNextN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Le Steak by Chef Amri'     # Most expensive
    assert clean_data[4]['name'] == 'Go2Eat'


# Mergesort
def test_case_4(data):
    temp_data = MergeSort.MergeSort(data, 'distance', True)
    assert len(temp_data.list) == 54259
    clean_data = temp_data.GetNextN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Michin Korean Bbq & Hotpot'    # Top shortest distance
    assert clean_data[4]['name'] == 'Mushroom Cafe'

    clean_data = temp_data.GetNextN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Mushroom Cafe'
    assert clean_data[4]['name'] == 'Essen, the Anchorvale'

    clean_data = temp_data.GetPrevN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Michin Korean Bbq & Hotpot'
    assert clean_data[4]['name'] == 'Mushroom Cafe'

    temp_data.ChangeField('recommendation')     # Check ChangeField and ChangeOrder
    temp_data.ChangeOrder(False)
    clean_data = temp_data.GetNextN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Nylon Coffee Roasters'     # Top Recommendation score
    assert clean_data[4]['name'] == 'Ps.Cafe'

    temp_data = MergeSort.MergeSort(data, 'recommendation', False)
    assert len(temp_data.list) == 54259
    clean_data = temp_data.GetNextN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Nylon Coffee Roasters'     # Top Recommendation score
    assert clean_data[4]['name'] == 'Ps.Cafe'


# QuickSelect
def test_case_5(data):
    temp_data = QuickSelect.QuickSelect(data, 'distance', True)
    assert len(temp_data.data) == 54259
    clean_data = temp_data.GetNextN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Michin Korean Bbq & Hotpot'    # Top shortest distance
    assert clean_data[4]['name'] == 'Mushroom Cafe'

    clean_data = temp_data.GetNextN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Mushroom Cafe'
    assert clean_data[4]['name'] == 'Essen, the Anchorvale'

    clean_data = temp_data.GetPrevN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Michin Korean Bbq & Hotpot'
    assert clean_data[4]['name'] == 'Mushroom Cafe'

    temp_data.ChangeField('recommendation')     # Check ChangeField and ChangeOrder
    temp_data.ChangeOrder(False)
    clean_data = temp_data.GetNextN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Nylon Coffee Roasters'     # Top Recommendation score
    assert clean_data[4]['name'] == 'Ps.Cafe'

    temp_data = QuickSelect.QuickSelect(data, 'recommendation', False)
    assert len(temp_data.data) == 54259
    clean_data = temp_data.GetNextN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Nylon Coffee Roasters'     # Top Recommendation score
    assert clean_data[4]['name'] == 'Ps.Cafe'