from typing import List
from project.customer import Customer
from project.equipment import Equipment
from project.trainer import Trainer
from project.subscription import Subscription
from project.exercise_plan import ExercisePlan


class Gym:

    def __init__(self):
        self.customers: List[Customer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []
        self.trainers: List[Trainer] = []

    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)

    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) -> None:
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def subscription_info(self, subscription_id: int) -> str:
        subscription = next(filter(lambda s: s.id == subscription_id, self.subscriptions))
        customer = next(filter(lambda c: c.id == subscription.customer_id, self.customers))
        trainer = next(filter(lambda t: t.id == subscription.trainer_id, self.trainers))
        plan = next(filter(lambda p: p.id == subscription.exercise_id, self.plans))
        equipment = next(filter(lambda e: e.id == plan.equipment_id, self.equipment))

        return f"{str(subscription)}\n{str(customer)}\n{str(trainer)}\n{str(equipment)}\n{str(plan)}"
