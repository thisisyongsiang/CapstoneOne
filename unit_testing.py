import pytest
import json
import CategoryAndFilter as ct
import Heapsort
import MergeSort


@pytest.fixture
def data():
    dir="yelpAPIData.json"
    f=open(dir,encoding='utf-8')
    data=json.load(f)

    # Get Base Data to display first
    clean_data = ct.simplifyData(data)
    return clean_data


# simplifyData returns correct results
def test_case_1(data):
    assert len(data) == 1000
    assert data[0]['name'] == 'Ikura Japanese'
    assert data[999]['name'] == 'Turf City Canteen'


# Filter data by field and value range
def test_case_2(data):
    clean_data = ct.filterDataByFieldAndValueRange(data, 'distance', [0, 40000])
    assert len(clean_data) == 999   # one restaurant is closed

    clean_data = ct.filterDataByFieldAndValueRange(data, 'distance', [0, 267])
    assert len(clean_data) == 1

    clean_data = ct.filterDataByFieldAndValueRange(data, 'distance', [0, 300])
    assert len(clean_data) == 7


# Heapsort
def test_case_3(data):
    temp_data = Heapsort.getItemsByField(data, 'distance', True)
    assert len(temp_data.arr) == 1000
    clean_data = temp_data.getTopN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Ikura Japanese'
    assert clean_data[4]['name'] == 'Starbucks'

    temp_data = Heapsort.getItemsByField(data, 'recommendation', False)
    assert len(temp_data.arr) == 1000
    clean_data = temp_data.getTopN(5)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Two Men Bagel House'
    assert clean_data[4]['name'] == 'Dian Xiao Er'  # Not sorted by distance


# Mergesort
def test_case_4(data):
    clean_data = MergeSort.getFirstN(data, 'distance', 5, True)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Ikura Japanese'
    assert clean_data[4]['name'] == 'Starbucks'

    clean_data = MergeSort.getFirstN(data, 'recommendation', 5, False)
    assert len(clean_data) == 5
    assert clean_data[0]['name'] == 'Two Men Bagel House'
    assert clean_data[4]['name'] == "Chef Kang's Noodle House"  # Not sorted by distance