#cpickle.py
import cPickle as p
shop_list_file = 'shoplist.data'
shoplist = {'1':'apple','2':'phone','3':'papper','4':'meat'}
f = file(shop_list_file,'w')
p.dump(shoplist,f)
f.close()
f= file(shop_list_file)
store = p.load(f)
print store
f.close()
