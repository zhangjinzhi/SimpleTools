# -*- coding:utf-8 -*-
import geocoder
#功能一：地理编码
g = geocoder.google("1403 Washington Ave, New Orleans, LA 70130")
print g.latlng
print g.ok
#print g.geojson
g = geocoder.arcgis(u"北京市海淀区上地十街10号")
print g.latlng
#print g.geojson

print
#逆地理编码
#Google的地址信息很全面
g = geocoder.google([29.9287839, -90.08421849999999], method='reverse')
print g.address
print g.city
print g.state
print g.country
#Google的地址信息很全面
g = geocoder.google([40.050934, 116.30079], method='reverse')
print g.address
print g.city
print g.state
print g.country
#arcgis的地址信息提供的不全面
g = geocoder.arcgis([40.050934, 116.30079], method='reverse')
print g.address
print g.city
print g.state
print g.country

print
#功能二：查询ip
g = geocoder.ip('199.7.157.0')  #指定ip的地址，查询经纬度和城市
print g.latlng
print g.city
g = geocoder.ip('me')           #根据自己所在地，查询经纬度和城市
print g.latlng
print g.city

print
#查询一个城市的空间包围盒
g = geocoder.arcgis(u"湖北")
print g.bbox