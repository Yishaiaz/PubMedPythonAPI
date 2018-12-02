import requests
import xml.etree.ElementTree as et


def ids_by_query(query: str="food poisoning")-> list:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    r = requests.get(url + "esearch.fcgi?term=" + "autism")
    xml_res_tree = et.fromstring(r.content)
    ids_list = []
    for item in xml_res_tree.iter('IdList'):
        for data in item.iter('Id'):
            ids_list.append(data.text)

    return ids_list


def summary_by_ids(database: str= "nucest", ids_list: list = []):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    ids_list_to_string=""
    for item in ids_list:
        ids_list_to_string += f"{item},"
    ids_list_to_string = ids_list_to_string[:-1]
    r = requests.get(url+f"esummary.fcgi?db={database}&id={ids_list_to_string}")
    return et.fromstring(r.content)


def docsum_to_str(xmltree):
    ans=""
    for item in xmltree.iter('DocSum'):
        for inner_item in item.iter('Item'):
            ans += f"{inner_item.text}, {inner_item.attrib}\n"

    return ans


if __name__ == '__main__':
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    try1 = "einfo.fcgi"
    # r = requests.get(url+try1)
    # xml_res_tree = et.fromstring(r.content)
    # print(xml_res_tree)
    # xml_res_tree = xml_res_tree[0]
    # for item in xml_res_tree.iter('DbList'):
    #     for data in item.iter('DbName'):
    #         print(f"{data.tag}, {data.attrib}, {data.text} \n")

    ids = ids_by_query()
    results = docsum_to_str(summary_by_ids(ids_list=ids))
    print(results)




