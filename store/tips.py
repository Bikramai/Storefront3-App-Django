# Preload related objects
from store.models import Product

#Optimizations
# -Optimize the Python code
# -Re-write the queryset
# -Tune the database redesign the tables
# -Cache the result - store the result in memory
# -Buy more hardware

#optimize the critical parts


Product.objects.select_related('...')
Product.objects.prefetch_related('...')

# Load only what you need
Product.objects.only('title')
Product.objects.defer('description')

# Use values
Product.objects.values()
Product.objects.values_list()

# Count properly
Product.objects.count()
len(Product.objects.all()) #BAD

# Bulk create/update
Product.objects.bulk_create([])
