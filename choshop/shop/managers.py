from core.shared import ActiveManager

class ProductCategoryManager(ActiveManager):    
    def get_by_natural_key(self, slug):
        return self.get(slug=slug)