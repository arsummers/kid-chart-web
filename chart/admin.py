from django.contrib import admin
from .models import Kid, Reward, Rule, RuleInstance

@admin.register(Kid)
class KidAdmin(admin.ModelAdmin):
    pass

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    pass

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    pass

@admin.register(RuleInstance)
class RuleInstanceAdmin(admin.ModelAdmin):
    pass