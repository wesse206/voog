import { Routes } from '@angular/router';
import { AfwesigOnderwyserComponent } from './afwesig-onderwyser/afwesig-onderwyser.component';
import { HomeComponent } from './home/home.component';
import { VoogComponent } from './voog/voog.component';
import { VindLeerderComponent } from './vind-leerder/vind-leerder.component';

export const routes: Routes = [
    { path: '', component: HomeComponent},
    { path: 'onderwyser-afwesig', component: AfwesigOnderwyserComponent },
    { path: 'voog', component: VoogComponent},
    { path: 'vind-leerder', component: VindLeerderComponent}
];
